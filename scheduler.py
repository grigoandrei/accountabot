import schedule
import time
from task_manager import list_tasks
from rich import print
from plyer import notification

def daily_checkin():
    tasks = list_tasks()
    pending = [t for t in tasks if t[2] == 0]
    message = ""
    if not pending:
        message = "You have no pending tasks! Great job!"
    else:
        message = f"You have {len(pending)} pending tasks. Check your task list!"
    notification.notify(
        title="AccountaBot Check-in",
        message=message,
        timeout=10
    )
    print("\n[bold green]Daily Check-in sent![/bold green]")

# Schedule to run every 30 seconds (for testing)
schedule.every().day.at("21:00").do(daily_checkin)

print("Scheduler started. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
