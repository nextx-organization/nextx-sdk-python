from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.action_item_dto import ActionItemDto





T = TypeVar("T", bound="CallSummaryAiDto")



@_attrs_define
class CallSummaryAiDto:
    

    call_id: UUID | Unset = UNSET
    summary: None | str | Unset = UNSET
    sentiment: None | str | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    keywords_detected: list[str] | None | Unset = UNSET
    action_items: list[ActionItemDto] | None | Unset = UNSET
    analysis_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.action_item_dto import ActionItemDto # noqa: PLC0415
        call_id: str | Unset = UNSET
        if not isinstance(self.call_id, Unset):
            call_id = str(self.call_id)

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        sentiment: None | str | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        keywords_detected: list[str] | None | Unset
        if isinstance(self.keywords_detected, Unset):
            keywords_detected = UNSET
        elif isinstance(self.keywords_detected, list):
            keywords_detected = self.keywords_detected


        else:
            keywords_detected = self.keywords_detected

        action_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.action_items, Unset):
            action_items = UNSET
        elif isinstance(self.action_items, list):
            action_items = []
            for action_items_type_0_item_data in self.action_items:
                action_items_type_0_item = action_items_type_0_item_data.to_dict()
                action_items.append(action_items_type_0_item)


        else:
            action_items = self.action_items

        analysis_status: None | str | Unset
        if isinstance(self.analysis_status, Unset):
            analysis_status = UNSET
        else:
            analysis_status = self.analysis_status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if sentiment_score is not UNSET:
            field_dict["sentimentScore"] = sentiment_score
        if keywords_detected is not UNSET:
            field_dict["keywordsDetected"] = keywords_detected
        if action_items is not UNSET:
            field_dict["actionItems"] = action_items
        if analysis_status is not UNSET:
            field_dict["analysisStatus"] = analysis_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_item_dto import ActionItemDto # noqa: PLC0415
        d = dict(src_dict)
        _call_id = d.pop("callId", UNSET)
        call_id: UUID | Unset
        if isinstance(_call_id,  Unset):
            call_id = UNSET
        else:
            call_id = UUID(_call_id)




        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_sentiment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))


        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentimentScore", UNSET))


        def _parse_keywords_detected(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_detected_type_0 = cast(list[str], data)

                return keywords_detected_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords_detected = _parse_keywords_detected(d.pop("keywordsDetected", UNSET))


        def _parse_action_items(data: object) -> list[ActionItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                action_items_type_0 = []
                _action_items_type_0 = data
                for action_items_type_0_item_data in (_action_items_type_0):
                    action_items_type_0_item = ActionItemDto.from_dict(action_items_type_0_item_data)



                    action_items_type_0.append(action_items_type_0_item)

                return action_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActionItemDto] | None | Unset, data)

        action_items = _parse_action_items(d.pop("actionItems", UNSET))


        def _parse_analysis_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analysis_status = _parse_analysis_status(d.pop("analysisStatus", UNSET))


        call_summary_ai_dto = cls(
            call_id=call_id,
            summary=summary,
            sentiment=sentiment,
            sentiment_score=sentiment_score,
            keywords_detected=keywords_detected,
            action_items=action_items,
            analysis_status=analysis_status,
        )

        return call_summary_ai_dto

