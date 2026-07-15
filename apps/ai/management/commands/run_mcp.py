import os
from django.core.management.base import BaseCommand
from mcp.server.fastmcp import FastMCP
from apps.orders.models import Order
from apps.shipments.models import Shipment
from asgiref.sync import sync_to_async

mcp = FastMCP("ACRON Core AI Engine")

@mcp.tool()
async def get_order_status(order_uuid: str) -> str:
    """
    Get the current billing/payment status of an order using its UUID.
    """
    # خواندن متغیر محیطیِ امن که توسط جنگو ست شده است
    user_id = os.environ.get("ACRON_USER_ID")
    if not user_id:
        return "خطای امنیتی: کاربر احراز هویت نشده است."

    @sync_to_async
    def fetch_order():
        try:
            # 🛡️ دیوار امنیتی: بررسی دسترسی کاربر به سفارش
            # اگر مدل سفارش شما مستقیماً به User متصل است، از فیلتر زیر استفاده کنید:
            # order = Order.objects.get(id=order_uuid, user_id=user_id)
            
            # اگر مدل سفارش شما از طریق Customer به User متصل است:
            order = Order.objects.get(id=order_uuid, customer__user_id=user_id)
            
            return f"سفارش شماره {order_uuid} در وضعیت [{order.get_status_display()}] قرار دارد."
        except Order.DoesNotExist:
            return "خطا: سفارشی با این شناسه برای شما یافت نشد یا شما دسترسی ندارید."
        except Exception as e:
            return f"خطای غیرمنتظره در سیستم: {str(e)}"
            
    return await fetch_order()


@mcp.tool()
async def track_shipment_status(order_uuid: str) -> str:
    """
    Track the physical shipping status, carrier info, and tracking code for an order.
    """
    user_id = os.environ.get("ACRON_USER_ID")
    if not user_id:
        return "خطای امنیتی: کاربر احراز هویت نشده است."

    @sync_to_async
    def fetch_shipment():
        try:
            # 🛡️ دیوار امنیتی: بررسی دسترسی کاربر به مرسوله از طریق سفارش
            # اگر سفارش مستقیم به User وصل است:
            # shipment = Shipment.objects.get(order__id=order_uuid, order__user_id=user_id)
            
            # اگر سفارش به Customer و مشتری به User وصل است:
            shipment = Shipment.objects.get(order__id=order_uuid, order__customer__user_id=user_id)
            
            tracking_code = shipment.tracking_number or "هنوز صادر نشده است"
            tracking_link = shipment.get_tracking_url() or "لینک پیگیری موجود نیست"
            
            return (
                f"وضعیت ارسال: {shipment.get_status_display()}\n"
                f"شرکت حمل و نقل: {shipment.get_carrier_display()}\n"
                f"کد رهگیری پستی: {tracking_code}\n"
                f"لینک مستقیم پیگیری: {tracking_link}"
            )
        except Shipment.DoesNotExist:
            return "اطلاعات مرسوله یافت نشد. ممکن است این سفارش متعلق به شما نباشد یا هنوز صادر نشده باشد."
        except Exception as e:
            return f"خطای غیرمنتظره در سیستم: {str(e)}"
            
    return await fetch_shipment()


class Command(BaseCommand):
    help = "Starts the ACRON Model Context Protocol (MCP) Server"
    requires_system_checks = []

    def handle(self, *args, **options):
        self.stderr.write(self.style.SUCCESS("🤖 سرور هوش مصنوعی ACRON (MCP) روشن شد..."))
        mcp.run(transport="stdio")


