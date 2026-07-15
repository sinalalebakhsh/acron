import sys
import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_test_client():
    # ----------------- 🧪 آزمایشگاه امنیت -----------------
    # سناریو ۱: شناسه کاربری که در دیتابیس مالک سفارش "6d8c603e-fcde-44e2-9fe6-f93c87971948" است را وارد کنید (مثلاً "1")
    # سناریو ۲: شناسه یک کاربر دیگر یا یک کاربر فرضی (مثلاً "99") را بگذارید تا هک را شبیه‌سازی کنید!
    logged_in_user_id = "1" 
    # -----------------------------------------------------

    env_vars = os.environ.copy()
    env_vars["ACRON_USER_ID"] = logged_in_user_id

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "manage.py", "run_mcp"], 
        env=env_vars
    )
    
    print("⏳ در حال اتصال به سرور هوش مصنوعی ACRON...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("✅ اتصال با موفقیت برقرار شد!\n")
                
                # برای تست، از همان شناسه سفارش قبلی استفاده می‌کنیم
                target_order_id = "6d8c603e-fcde-44e2-9fe6-f93c87971948" 
                print(f"🤖 [شبیه‌سازی LLM]: در حال فراخوانی ابزار برای سفارش {target_order_id} با شناسه کاربر لود شده: {logged_in_user_id}...")
                
                result = await session.call_tool(
                    "track_shipment_status", 
                    arguments={"order_uuid": target_order_id}
                )
                
                print("\n📥 پاسخ دریافتی:")
                print(result.content[0].text)
                
    except Exception as e:
        print(f"❌ خطایی در کلاینت رخ داد: {e}")

if __name__ == "__main__":
    asyncio.run(run_test_client())




