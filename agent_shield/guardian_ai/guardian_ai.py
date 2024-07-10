# """ Built-in modules """
import json
from typing import Dict, Any, List, Optional

# """ Third-party modules """
from langchain.agents.agent import AgentExecutor
from langchain_core.runnables import RunnablePassthrough
from langchain_core.callbacks import BaseCallbackHandler

# """ Local modules """
from .llm_base import LLMBase, handel_output
from .guardian_category import GuardianCategory
from .prompt import DETECTION_PROMPT
from logs import BirdLogger


logger = BirdLogger("GuardianAI")


class BotException(Exception):
    """
    Custom exception class for the GuardianAI.
    """
    pass


class GuardianAI(LLMBase):
    """
    GuardianAI is the AI Assistant that is used by the Researcher to answer the user's questions.
    """

    _chain: Optional[AgentExecutor] = None

    @property
    def chain(self) -> AgentExecutor:
        """
        Get the chain instance.

        Returns:
            AgentExecutor: The chain instance.
        """
        if self._chain is None:
            guardian_categories = '\n\n'.join(
                [str(ctg) for ctg in GuardianCategory])
            self._chain = (
                DETECTION_PROMPT.partial(guardian_categories=guardian_categories) |
                self.llm
            )

        return self._chain

    def __init__(self) -> None:
        """
        Initialize the GuardianAI with the necessary configurations.

        Returns:
            None
        """
        # Initialize the parent class
        super().__init__()

    def invoke(self, question: str, callbacks: Optional[List[BaseCallbackHandler]] = None, **kwargs) -> Dict[str, Any]:
        """
        Invoke the AI Assistant to answer the user's question.

        Args:
            question (str): The user's input/question.
            callbacks (Optional[List[BaseCallbackHandler]]): The list of callback handlers.
            kwargs (Dict[str, Any]): The keyword arguments.

        Returns:
            Dict[str, Any]: The response as a dictionary.
        """
        try:
            # Create the response
            response = {
                "question": question,
            }
            # Predict the question
            llm = self.chain.invoke({'input': question}, {
                'callbacks': callbacks
            })
            # Add the llm results to the response
            response['results'] = {'llm': {
                'input': question,
                'output': llm,
            }, 'category': None}

            # handle the output
            output = handel_output(llm)
            # Get the answer
            classification_category = output.get('category', None)
            # Get the harm category
            category = GuardianCategory.from_type(classification_category)
            # Set the harm category into the response
            response['results']['category'] = category.to_map()
            return response
        except Exception as e:
            logger.error(f"Error invoking the AI Assistant: {e}")
            raise BotException(f"Error invoking the AI Assistant: {e}") from e
