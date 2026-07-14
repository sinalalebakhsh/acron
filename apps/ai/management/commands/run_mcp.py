from django.core.management.base import BaseCommand
from mcp.server.fastmcp import FastMCP
from apps.orders.models import Order
from apps.shipments.models import Shipment

# ۱. مقداردهی اولیه سرور MCP با یک نام مشخص
mcp = FastMCP("ACRON Core AI Engine")

# ۲. معرفی اولین ابزار (Tool) به هوش مصنوعی: خواندن وضعیت فاکتور
@mcp.tool()
def get_order_status(order_uuid: str) -> str:
    """
    Get the current billing/payment status of an order using its UUID.
    """
    try:
        order = Order.objects.get(id=order_uuid)
        return f"سفارش شماره {order_uuid} در وضعیت [{order.get_status_display()}] قرار دارد."
    except Order.DoesNotExist:
        return "خطا: سفارشی با این شناسه یافت نشد."

# ۳. معرفی دومین ابزار: پیگیری مرسوله پستی در انبار برای مشتری
@mcp.tool()
def track_shipment_status(order_uuid: str) -> str:
    """
    Track the physical shipping status, carrier info, and tracking code for an order.
    """
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


# ۴. ساخت دستور جنگو برای روشن نگه‌داشتن سرور
class Command(BaseCommand):
    help = "Starts the ACRON Model Context Protocol (MCP) Server"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("🤖 سرور هوش مصنوعی ACRON (MCP) با موفقیت روی پروتکل STDIO روشن شد..."))
        # سرور به صورت استاندارد روی ورودی/خروجی سیستم (Standard Input/Output) منتظر دستورات LLM می‌ماند
        mcp.run(transport="stdio")
    

