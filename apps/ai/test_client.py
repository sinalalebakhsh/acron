import sys  # <--- اضافه کردن کتابخانه سیستم برای خواندن مسیر پایتون فعال
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_test_client():
    # استفاده از sys.executable تضمین می‌کند که از پایتونِ فعال در pipenv استفاده شود
    # 🟢 تغییر مهم: اضافه کردن "-u" برای غیرفعال کردن بافر در ویندوز
    server_params = StdioServerParameters(
        command=sys.executable, 
        args=["-u","manage.py", "run_mcp"],
    )
    
    print("⏳ در حال اتصال به سرور هوش مصنوعی ACRON...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # دست دادن اولیه با سرور (Handshake)
                await session.initialize()
                print("✅ اتصال با موفقیت برقرار شد!\n")
                
                # دریافت لیست ابزارها
                tools_response = await session.list_tools()
                print("🛠️ ابزارهای معرفی شده به هوش مصنوعی:")
                for tool in tools_response.tools:
                    print(f"  - نام ابزار: {tool.name} | کاربرد: {tool.description}")
                
                print("\n" + "="*50 + "\n")
                
                # فرض کنیم می‌خواهیم اولین سفارش داخل دیتابیس را تست کنیم
                # در صورت نیاز شناسه سفارش خود را جایگزین کنید
                target_order_id = "6d8c603e-fcde-44e2-9fe6-f93c87971948" 
                
                print(f"🤖 [شبیه‌سازی LLM]: در حال فراخوانی ابزار برای سفارش {target_order_id}...")
                
                result = await session.call_tool(
                    "track_shipment_status", 
                    arguments={"order_uuid": target_order_id}
                )
                
                print("\n📥 پاسخ دریافتی از دیتابیس جنگو:")
                print(result.content[0].text)
                
    except Exception as e:
        print(f"❌ خطایی در کلاینت رخ داد: {e}\n❌ An error occurred in the client: unhandled errors in a TaskGroup (1 sub-exception)")

if __name__ == "__main__":
    asyncio.run(run_test_client())



