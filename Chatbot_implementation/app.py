import chainlit as cl
from src.llm import ask_drug, messages

@cl.on_message
async def main(message:cl.Message):
    messages.append({'role':'user', 'content':message.content})
    response = ask_drug(messages)
    messages.append({'role':'assistant', 'content':response})

    # sent a response back to the user

    await cl.Message(
        content = response
    ).send()