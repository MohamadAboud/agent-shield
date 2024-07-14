from enum import Enum
import json


class GuardianCategory(Enum):
    """ 
    The GuardianCategory enum for message categories.
    """
    HARM_CATEGORY_UNSPECIFIED = (
        0,
        "Category is unspecified.\nContent that does not fit into any specified harm category. This could include general or neutral messages that do not exhibit harmful or sensitive content."
    )
    HARM_CATEGORY_DEROGATORY = (
        1,
        "Negative or harmful comments targeting identity and/or protected attribute.\nIncludes insults, slurs, or derogatory remarks aimed at race, ethnicity, religion, gender, sexual orientation, disability, etc."
    )
    HARM_CATEGORY_TOXICITY = (
        2,
        "Content that is rude, disrespectful, or profane.\nMessages that exhibit rudeness, disrespect, or use of profanity. This category encompasses language or expressions that are socially unacceptable or offensive in nature."
    )
    HARM_CATEGORY_VIOLENCE = (
        3,
        "Describes scenarios depicting violence against an individual or group, or general descriptions of gore.\nIncludes descriptions or depictions of physical harm, injury, or violence towards others."
    )
    HARM_CATEGORY_CHILD_SEXUAL = (
        4,
        "Contains references to child sexual abuse or exploitation.\nMessages containing explicit references or descriptions related to child sexual abuse."
    )
    HARM_CATEGORY_SEXUAL = (
        5,
        "Contains references to sexual acts or other lewd content.\nMessages containing explicit sexual references or lewd content. This category includes discussions or descriptions of sexual acts, sexual behavior, or sexually suggestive language."
    )
    HARM_CATEGORY_MEDICAL = (
        6,
        "Promotes unchecked medical advice.\nContains advice or information related to health or medical treatments that may be unverified or dangerous."
    )
    HARM_CATEGORY_DANGEROUS = (
        7,
        "Dangerous content that promotes, facilitates, or encourages harmful acts.\nMessages that encourage or promote dangerous activities or behaviors."
    )
    HARM_CATEGORY_HARASSMENT = (
        8,
        "Harassment content.\nMessages intended to harass, intimidate, or threaten others."
    )
    HARM_CATEGORY_HATE_SPEECH = (
        9,
        "Hate speech and content.\nMessages that promote hatred or violence against individuals or groups based on race, ethnicity, religion, gender, sexual orientation, disability, etc."
    )
    HARM_CATEGORY_SEXUALLY_EXPLICIT = (
        10,
        "Sexually explicit content.\nMessages containing explicit sexual content or descriptions."
    )
    HARM_CATEGORY_DANGEROUS_CONTENT = (
        11,
        "Dangerous content.\nContent that poses a direct threat to physical or mental well-being."
    )
    PERSONAL_INFORMATION = (
        12,
        "Message contains personal information like phone numbers, names, addresses, etc.\nMessages that disclose private or confidential information about individuals."
    )
    NORMAL = (
        13,
        "The message content is normal and does not fall under any of the above categories.\nContent that is neutral and does not contain harmful or sensitive material."
    )

    def __new__(cls, num, description):
        obj = object.__new__(cls)
        obj._value_ = num
        obj.__description = description
        return obj
    
    @property
    def description(self) -> str:
        return self.__description
    

    @classmethod
    def from_type(cls, type: str | int) -> "GuardianCategory":
        """
        Get the GuardianCategory from the string or number.

        Args:
            type (str | int): The name or number of the GuardianCategory.

        Returns:
            GuardianCategory: The GuardianCategory.
        """
        for category in cls:
            if isinstance(type, str):
                if category.name.lower() == type.lower():
                    return category
            elif isinstance(type, int):
                if category.value == type:
                    return category
        return cls.HARM_CATEGORY_UNSPECIFIED
    
    
    def __str__(self) -> str:
        return f"{self.value}. {self.name} ({self.value}): {self.description}"
    
    def to_map(self) -> dict:
        return {
            "name": self.name,
            "value": self.value,
            "description": self.description
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_map())
