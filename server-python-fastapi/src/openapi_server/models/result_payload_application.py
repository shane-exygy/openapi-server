# coding: utf-8

"""
    minimal-sample-program

    desc

    The version of the OpenAPI document: 33
    Contact: civiform-dev@exygy.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.result_payload_application_sample_date_question import ResultPayloadApplicationSampleDateQuestion
from openapi_server.models.result_payload_application_sample_name_question import ResultPayloadApplicationSampleNameQuestion
from openapi_server.models.result_payload_application_sample_text_question_e import ResultPayloadApplicationSampleTextQuestionE
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResultPayloadApplication(BaseModel):
    """
    ResultPayloadApplication
    """ # noqa: E501
    sample_date_question: Optional[ResultPayloadApplicationSampleDateQuestion] = None
    sample_name_question: Optional[ResultPayloadApplicationSampleNameQuestion] = None
    sample_name_question___a: Optional[ResultPayloadApplicationSampleNameQuestion] = None
    sample_name_question__g: Optional[ResultPayloadApplicationSampleNameQuestion] = None
    sample_text_question__e: Optional[ResultPayloadApplicationSampleTextQuestionE] = None
    __properties: ClassVar[List[str]] = ["sample_date_question", "sample_name_question", "sample_name_question___a", "sample_name_question__g", "sample_text_question__e"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResultPayloadApplication from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of sample_date_question
        if self.sample_date_question:
            _dict['sample_date_question'] = self.sample_date_question.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sample_name_question
        if self.sample_name_question:
            _dict['sample_name_question'] = self.sample_name_question.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sample_name_question___a
        if self.sample_name_question___a:
            _dict['sample_name_question___a'] = self.sample_name_question___a.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sample_name_question__g
        if self.sample_name_question__g:
            _dict['sample_name_question__g'] = self.sample_name_question__g.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sample_text_question__e
        if self.sample_text_question__e:
            _dict['sample_text_question__e'] = self.sample_text_question__e.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResultPayloadApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sample_date_question": ResultPayloadApplicationSampleDateQuestion.from_dict(obj.get("sample_date_question")) if obj.get("sample_date_question") is not None else None,
            "sample_name_question": ResultPayloadApplicationSampleNameQuestion.from_dict(obj.get("sample_name_question")) if obj.get("sample_name_question") is not None else None,
            "sample_name_question___a": ResultPayloadApplicationSampleNameQuestion.from_dict(obj.get("sample_name_question___a")) if obj.get("sample_name_question___a") is not None else None,
            "sample_name_question__g": ResultPayloadApplicationSampleNameQuestion.from_dict(obj.get("sample_name_question__g")) if obj.get("sample_name_question__g") is not None else None,
            "sample_text_question__e": ResultPayloadApplicationSampleTextQuestionE.from_dict(obj.get("sample_text_question__e")) if obj.get("sample_text_question__e") is not None else None
        })
        return _obj


