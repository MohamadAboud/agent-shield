import os
import json
from typing import Optional
from dotenv import load_dotenv
from agent_shield.guardian_ai.guardian_ai import GuardianAI
from agent_shield.guardian_ai.llm_base import LLMBase
from agent_shield.guardian_ai.guardian_category import GuardianCategory
load_dotenv(override=True)  # Load environment variables from .env file


try:
    import chainlit as cl
except ImportError:
    raise Exception(
        "Please install chainlit using `pip install chainlit==1.1.305`")


@cl.set_chat_profiles
async def chat_profile(current_user: cl.User):
    return [
        cl.ChatProfile(
            name=LLMBase.BASE_MODEL_NAME,  # gemini-1.5-flash
            markdown_description="The underlying LLM model is **Gemini**, which is a powerful language model capable of generating human-like text responses.",
            icon="public/logo.svg",
        ),
    ]


@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="رسالة استفزازية",
            message="أنت أحمق حقاً، هل تعلم أنك تجعلني أغضب بشدة عندما أسمع هذا منك؟ لا أستطيع تحمل تصرفاتك السيئة بعد الآن.",
            icon="public/logo.svg",
        ),
        cl.Starter(
            label="رسالة مسيئة",
            message="أنت سيء جداً، هل تعلم أنك تؤثر سلباً على مزاجي كلما رأيتك؟ لا يمكنني التعامل مع هذا المستوى من السلوك.",
            icon="public/logo.svg",
        ),
        cl.Starter(
            label="معلومات شخصية",
            message="إذا أردت التحدث معي، يمكنك الاتصال بي على رقمي 00962777777777، أنا في انتظار مكالمتك لمزيد من الحديث.",
            icon="public/logo.svg",
        ),
        cl.Starter(
            label="رسالة تهديد",
            message="إذا كنت رجل حقيقي، تعال لقابلتي خارج المنزل، لنرى من هو الأقوى والأذكى بيننا.",
            icon="public/logo.svg",
        ),
    ]


# ...

@cl.on_chat_start
async def on_chat_start():
    # Instantiate the GuardianAI instance
    chain = GuardianAI()

    cl.user_session.set("chain", chain)


@cl.action_callback("category_info")
async def on_action(action):
    await cl.Message(content=json.loads(action.value), author="Aboud").send()
    # Optionally remove the action button from the chatbot user interface
    await action.remove()


@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")  # type: GuardianAI

    try:
        res = chain.invoke(
            question=message.content,
            callbacks=[cl.LangchainCallbackHandler()],
        )

        actions = [
            cl.Action(
                name="category_info",
                label="Category Info",
                value=GuardianCategory.from_type(
                    res['results']['category']
                ).to_json(),
                description="Get more information about the category",
            )
        ]

        await cl.Message(content=res, author="Aboud", actions=actions).send()
    except Exception as e:
        elements = [
            cl.Text(name="Error", content=str(e), display="inline")
        ]

        await cl.Message(
            content="",
            elements=elements,
        ).send()


def run(host: Optional[str] = None, port: Optional[int] = None) -> None:
    """
    Main function to run the app ui server.

    Args:
        host (str, optional): The host to run the server on.
        port (int, optional): The port to run the server on.

    Returns:
        None

    Raises:
        If the server could not be started.
    """
    from chainlit.cli import run_chainlit

    os.environ.setdefault("CHAINLIT_HOST", host or "0.0.0.0")
    os.environ.setdefault("CHAINLIT_PORT", str(port or 7652))
    run_chainlit(__file__)


if __name__ == '__main__':
    # Run the app
    run()
