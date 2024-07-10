# """ Built-in modules """
import re
import json
from typing import Optional
from enum import Enum

# """ Third-party modules """
from langchain_core.language_models.llms import BaseLLM
from langchain_google_genai import (
    GoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory
)


def handel_output(output: str) -> dict:
    """
        Handle the output from the model.

    Args:
        output (str): The output from the model.

    Returns:
        dict: The output as a dictionary.
    """
    # remove the ```, [any character]\n, ``` from the output
    output = re.sub(r"```[a-z]+\n", "", output)
    output = re.sub(r"```", "", output)
    # load the output as a json string
    output = json.loads(output)
    return output



class ModelName(Enum):
    """The ModelName class for the model names."""
    GEMINI_PRO = "gemini-pro"
    GEMINI_15_FLASH = "gemini-1.5-flash"
    GEMINI_15_PRO = "gemini-1.5-pro"


class LLMBase:
    """The LLMBase class for handling the LLMs."""

    # Model name
    BASE_MODEL_NAME: str = ModelName.GEMINI_15_FLASH.value

    # show the model thinking.
    VERBOSE: bool = True

    # The temperature of the model (creativity level)
    TEMPERATURE: float = 0.0

    # The LLM instance
    _llm: Optional[BaseLLM] = None

    @property
    def llm(self) -> BaseLLM:
        """
        Get the LLM instance.

        Returns:
            BaseLLM: The LLM instance.
        """
        # Check if the _llm has been initialized
        if self._llm is None:
            # Initialize the LLM.
            self._llm = GoogleGenerativeAI(
                model=self.BASE_MODEL_NAME,
                temperature=self.TEMPERATURE,
                verbose=self.VERBOSE,
                safety_settings={
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                }
            )
        return self._llm