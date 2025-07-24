import click
from task_manager import add_task, list_tasks, complete_task, delete_task
from db import init_db
from rich import print

def get_task_by_index(index):
    tasks = list_tasks()
    if 0 < index <= len(tasks):
        return tasks[index - 1]
    else:
        return None

@click.group()
def cli():
    """AccountaBot CLI - Your Productivity Assistant"""
    init_db()

@cli.command()
@click.argument('description')
def add(description):
    """Add new task"""
    add_task(description)
    print(f":white_check_mark: [green]Added task: [/green] {description}")

@cli.command()
def view():
    """View all tasks"""
    tasks = list_tasks()
    if not tasks:
        print("[yellow]No tasks found.[/yellow]")
        return
    
    print("[bold blue]Your Tasks:[/bold blue]")
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task[2] else "[ ]"
        print(f"{status} {idx}. {task[1]}")

@cli.command()
@click.argument('task_index', type=int)
def done(task_index):
    """Mark a task as done"""
    task = get_task_by_index(task_index)
    if task:
        complete_task(task[0])
        print(task[0])
        print(f":checkered_flag: [blue]Marked task {task_index} as done[/blue]")
    else:
        print(f"[red]Task {task_index} not found.[/red]")

@cli.command()
@click.argument('task_index', type=int)
def delete(task_index):
    """Delete a task by its number"""
    task = get_task_by_index(task_index)
    if task:
        delete_task(task[0])  # use real DB id
        print(f":wastebasket: [red]Deleted task {task_index}[/red]")
    else:
        print(f"[red]Task {task_index} not found.[/red]")


if __name__ == "__main__":
    cli()

