import click
from task_manager import add_task, list_tasks, complete_task, delete_task
from db import init_db
from rich import print

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
    for task in tasks:
        status = "[x]" if task[2] else "[ ]"
        print(f"{status} {task[0]}. {task[1]}")

@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    """Mark a task as done"""
    complete_task(task_id)
    print(f":checkered_flag: [blue]Marked task {task_id} as done[/blue]")

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task by its ID"""
    delete_task(task_id)
    print(f":wastebasket: [red]Deleted task {task_id}[/red]")

if __name__ == "__main__":
    cli()

