from django.core.management.base import BaseCommand
from mcp.server.fastmcp import FastMCP
from apps.orders.models import Order
from apps.shipments.models import Shipment
from asgiref.sync import sync_to_async  # 🟢 ۱. وارد کردن ابزار همگام‌سازی جنگو

mcp = FastMCP("ACRON Core AI Engine")

@mcp.tool()
async def get_order_status(order_uuid: str) -> str:  # 🟢 تبدیل به تابع async
    """
    Get the current billing/payment status of an order using its UUID.
    """
    # اجرای کوئری دیتابیس در یک ترد همگام ایمن
    @sync_to_async
    def fetch_order():
        try:
            order = Order.objects.get(id=order_uuid)
            return f"سفارش شماره {order_uuid} در وضعیت [{order.get_status_display()}] قرار دارد."
        except Order.DoesNotExist:
            return "خطا: سفارشی با این شناسه یافت نشد."
        except Exception as e:
            return f"خطای سیستم: {str(e)}"
            
    return await fetch_order()


@mcp.tool()
async def track_shipment_status(order_uuid: str) -> str:  # 🟢 تبدیل به تابع async
    """
    Track the physical shipping status, carrier info, and tracking code for an order.
    """
    # اجرای کوئری دیتابیس در یک ترد همگام ایمن
    @sync_to_async
    def fetch_shipment():
        try:
            shipment = Shipment.objects.get(order__id=order_uuid)
            tracking_code = shipment.tracking_number or "هنوز صادر نشده است"
            tracking_link = shipment.get_tracking_url() or "لینک پیگیری موجود نیست"
            
            return (
                f"وضعیت ارسال: {shipment.get_status_display()}\n"
                f"شرکت حمل و نقل: {shipment.get_carrier_display()}\n"
                f"کد رهگیری پستی: {tracking_code}\n"
                f"لینک مستقیم پیگیری: {tracking_link}"
            )
        except Shipment.DoesNotExist:
            return "این سفارش هنوز پرداخت نشده یا مرسوله‌ای برای آن در انبار صادر نشده است."
        except Exception as e:
            return f"خطای سیستم: {str(e)}"
            
    return await fetch_shipment()


class Command(BaseCommand):
    help = "Starts the ACRON Model Context Protocol (MCP) Server"
    
    requires_system_checks = []

    def handle(self, *args, **options):
        # نوشتن پیام فقط روی stderr
        self.stderr.write(self.style.SUCCESS("🤖 سرور هوش مصنوعی ACRON (MCP) روشن شد...\n🤖 ACRON AI Server (MCP) has been launched..."))
        mcp.run(transport="stdio")
    


