import argparse
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.utils.storage import load_users, save_users, user_path


def add_user(args):
    users = load_users(user_path)
    user = User(args.name, args.email)
    users.append(user)
    save_users(user_path, users)
    print(f"User '{args.name}' created!")


def add_project(args):
    users = load_users(user_path)

    for user in users:
        if user.name == args.user:
            project = Project(args.title, args.description, args.due_date)
            user.add_project(project)
            save_users(user_path, users)
            print("Project added!")
            return

    print("User not found")


def add_task(args):
    users = load_users(user_path)

    for user in users:
        for project in user.projects:
            if project.title == args.project:
                task = Task(args.title)
                project.add_task(task)
                save_users(user_path, users)
                print("Task added!")
                return
    print("Project not found")


def complete_task(args):
    users = load_users(user_path)

    for user in users:
        for project in user.projects:
            for task in project.tasks:
                if task.title == args.title:
                    task.complete()
                    save_users(user_path, users)
                    print("Task completed!")
                    return
    print("Task not found")


def list_users_and_data(args):
    users = load_users(user_path)
    for user in users:
        print(user)
        for project in user.projects:
            print(f"{project}")
            for task in project.tasks:
                print(f"{task}")


def main():
    parser = argparse.ArgumentParser(description="CLI Project Manager")
    subparsers = parser.add_subparsers()

    parser_user = subparsers.add_parser("add-user")
    parser_user.add_argument("--name", required=True)
    parser_user.add_argument("--email", required=True)
    parser_user.set_defaults(func=add_user)

    parser_project = subparsers.add_parser("add-project")
    parser_project.add_argument("--user", required=True)
    parser_project.add_argument("--title", required=True)
    parser_project.add_argument("--description", default="")
    parser_project.add_argument("--due_date", default=None)
    parser_project.set_defaults(func=add_project)

    parser_task = subparsers.add_parser("add-task")
    parser_task.add_argument("--project", required=True)
    parser_task.add_argument("--title", required=True)
    parser_task.set_defaults(func=add_task)

    parser_complete = subparsers.add_parser("complete-task")
    parser_complete.add_argument("--title", required=True)
    parser_complete.set_defaults(func=complete_task)

    parser_list = subparsers.add_parser("list-users")
    parser_list.set_defaults(func=list_users)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

