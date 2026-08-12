from dotenv import load_dotenv

load_dotenv()

from agent.tools import check_inventory, write_copy, schedule_post
from agent.prompts import SYSTEM_PROMPT

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

        scheduled = schedule_post(copy["copy"], POST_TIME)
        print("Scheduled:", scheduled)
    else:
        print(f"{toy_name} doesn't need promotion right now.")


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
