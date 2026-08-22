from dotenv import load_dotenv

load_dotenv()

from tools import check_inventory, write_copy, schedule_post, send_slack_approval
from prompts import SYSTEM_PROMPT

TOY_CATALOG = [
    "Rocket Building Blocks",
    "Cuddly Dino Plush",
    "Remote Control Race Car",
    "Rainbow Art Kit",
]

POST_TIME = "2026-08-15 09:00"

def handle_toy(toy_name: str):
    print(f"\nChecking inventory for: {toy_name}")
    stock = check_inventory(toy_name)
    print(stock)

    if stock["quantity"] > 50:
        print(f"{toy_name} is overstocked. Time to promote it!")

        copy = write_copy(toy_name, tone="fun and excited")
        print("Generated copy:", copy["copy"])

        # 1. Ask for human approval via Slack tool
        approval_status = send_slack_approval(copy["copy"], toy_name)
        print(approval_status)

        # 2. Only schedule if the human typed 'approve'
        if "Approved" in approval_status:
            scheduled = schedule_post(copy["copy"], POST_TIME)
            print("Scheduled:", scheduled)
        else:
            print(f"Skipping schedule for {toy_name}: Human rejected the draft.")


def run_agent():
    print("SYSTEM PROMPT:")
    print(SYSTEM_PROMPT)
    print(f"\nCatalog: {', '.join(TOY_CATALOG)}")
    print("Type a toy name to check its stock and (maybe) schedule a promo post.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        handle_toy(user_input)


if __name__ == "__main__":
    run_agent()
