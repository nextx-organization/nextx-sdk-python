from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.transcript_segment_dto import TranscriptSegmentDto





T = TypeVar("T", bound="CallTranscriptDto")



@_attrs_define
class CallTranscriptDto:
    

    call_id: UUID | Unset = UNSET
    transcript_status: None | str | Unset = UNSET
    segments: list[TranscriptSegmentDto] | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    analysis_status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.transcript_segment_dto import TranscriptSegmentDto # noqa: PLC0415
        call_id: str | Unset = UNSET
        if not isinstance(self.call_id, Unset):
            call_id = str(self.call_id)

        transcript_status: None | str | Unset
        if isinstance(self.transcript_status, Unset):
            transcript_status = UNSET
        else:
            transcript_status = self.transcript_status

        segments: list[dict[str, Any]] | None | Unset
        if isinstance(self.segments, Unset):
            segments = UNSET
        elif isinstance(self.segments, list):
            segments = []
            for segments_type_0_item_data in self.segments:
                segments_type_0_item = segments_type_0_item_data.to_dict()
                segments.append(segments_type_0_item)


        else:
            segments = self.segments

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

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
        if transcript_status is not UNSET:
            field_dict["transcriptStatus"] = transcript_status
        if segments is not UNSET:
            field_dict["segments"] = segments
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if analysis_status is not UNSET:
            field_dict["analysisStatus"] = analysis_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcript_segment_dto import TranscriptSegmentDto # noqa: PLC0415
        d = dict(src_dict)
        _call_id = d.pop("callId", UNSET)
        call_id: UUID | Unset
        if isinstance(_call_id,  Unset):
            call_id = UNSET
        else:
            call_id = UUID(_call_id)




        def _parse_transcript_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_status = _parse_transcript_status(d.pop("transcriptStatus", UNSET))


        def _parse_segments(data: object) -> list[TranscriptSegmentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segments_type_0 = []
                _segments_type_0 = data
                for segments_type_0_item_data in (_segments_type_0):
                    segments_type_0_item = TranscriptSegmentDto.from_dict(segments_type_0_item_data)



                    segments_type_0.append(segments_type_0_item)

                return segments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TranscriptSegmentDto] | None | Unset, data)

        segments = _parse_segments(d.pop("segments", UNSET))


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_analysis_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analysis_status = _parse_analysis_status(d.pop("analysisStatus", UNSET))


        call_transcript_dto = cls(
            call_id=call_id,
            transcript_status=transcript_status,
            segments=segments,
            completed_at=completed_at,
            analysis_status=analysis_status,
        )

        return call_transcript_dto

