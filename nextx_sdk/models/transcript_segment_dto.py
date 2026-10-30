from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TranscriptSegmentDto")



@_attrs_define
class TranscriptSegmentDto:
    

    speaker: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    start_ms: int | Unset = UNSET
    end_ms: int | Unset = UNSET
    confidence: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        speaker: None | str | Unset
        if isinstance(self.speaker, Unset):
            speaker = UNSET
        else:
            speaker = self.speaker

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        start_ms = self.start_ms

        end_ms = self.end_ms

        confidence = self.confidence


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if speaker is not UNSET:
            field_dict["speaker"] = speaker
        if text is not UNSET:
            field_dict["text"] = text
        if start_ms is not UNSET:
            field_dict["startMs"] = start_ms
        if end_ms is not UNSET:
            field_dict["endMs"] = end_ms
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_speaker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        speaker = _parse_speaker(d.pop("speaker", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        start_ms = d.pop("startMs", UNSET)

        end_ms = d.pop("endMs", UNSET)

        confidence = d.pop("confidence", UNSET)

        transcript_segment_dto = cls(
            speaker=speaker,
            text=text,
            start_ms=start_ms,
            end_ms=end_ms,
            confidence=confidence,
        )

        return transcript_segment_dto

