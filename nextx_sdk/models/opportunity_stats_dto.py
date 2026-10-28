from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.opportunity_forecast_dto import OpportunityForecastDto
  from ..models.pipeline_stage_distribution_dto import PipelineStageDistributionDto





T = TypeVar("T", bound="OpportunityStatsDto")



@_attrs_define
class OpportunityStatsDto:
    

    total_open: int | Unset = UNSET
    total_won: int | Unset = UNSET
    total_lost: int | Unset = UNSET
    total_estimated_value: float | Unset = UNSET
    total_won_value: float | Unset = UNSET
    new_in_period: int | Unset = UNSET
    win_rate: float | Unset = UNSET
    forecast: OpportunityForecastDto | Unset = UNSET
    pipeline_distribution: list[PipelineStageDistributionDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.opportunity_forecast_dto import OpportunityForecastDto # noqa: PLC0415
        from ..models.pipeline_stage_distribution_dto import PipelineStageDistributionDto # noqa: PLC0415
        total_open = self.total_open

        total_won = self.total_won

        total_lost = self.total_lost

        total_estimated_value = self.total_estimated_value

        total_won_value = self.total_won_value

        new_in_period = self.new_in_period

        win_rate = self.win_rate

        forecast: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast.to_dict()

        pipeline_distribution: list[dict[str, Any]] | None | Unset
        if isinstance(self.pipeline_distribution, Unset):
            pipeline_distribution = UNSET
        elif isinstance(self.pipeline_distribution, list):
            pipeline_distribution = []
            for pipeline_distribution_type_0_item_data in self.pipeline_distribution:
                pipeline_distribution_type_0_item = pipeline_distribution_type_0_item_data.to_dict()
                pipeline_distribution.append(pipeline_distribution_type_0_item)


        else:
            pipeline_distribution = self.pipeline_distribution


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if total_open is not UNSET:
            field_dict["totalOpen"] = total_open
        if total_won is not UNSET:
            field_dict["totalWon"] = total_won
        if total_lost is not UNSET:
            field_dict["totalLost"] = total_lost
        if total_estimated_value is not UNSET:
            field_dict["totalEstimatedValue"] = total_estimated_value
        if total_won_value is not UNSET:
            field_dict["totalWonValue"] = total_won_value
        if new_in_period is not UNSET:
            field_dict["newInPeriod"] = new_in_period
        if win_rate is not UNSET:
            field_dict["winRate"] = win_rate
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if pipeline_distribution is not UNSET:
            field_dict["pipelineDistribution"] = pipeline_distribution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opportunity_forecast_dto import OpportunityForecastDto # noqa: PLC0415
        from ..models.pipeline_stage_distribution_dto import PipelineStageDistributionDto # noqa: PLC0415
        d = dict(src_dict)
        total_open = d.pop("totalOpen", UNSET)

        total_won = d.pop("totalWon", UNSET)

        total_lost = d.pop("totalLost", UNSET)

        total_estimated_value = d.pop("totalEstimatedValue", UNSET)

        total_won_value = d.pop("totalWonValue", UNSET)

        new_in_period = d.pop("newInPeriod", UNSET)

        win_rate = d.pop("winRate", UNSET)

        _forecast = d.pop("forecast", UNSET)
        forecast: OpportunityForecastDto | Unset
        if isinstance(_forecast,  Unset):
            forecast = UNSET
        else:
            forecast = OpportunityForecastDto.from_dict(_forecast)




        def _parse_pipeline_distribution(data: object) -> list[PipelineStageDistributionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pipeline_distribution_type_0 = []
                _pipeline_distribution_type_0 = data
                for pipeline_distribution_type_0_item_data in (_pipeline_distribution_type_0):
                    pipeline_distribution_type_0_item = PipelineStageDistributionDto.from_dict(pipeline_distribution_type_0_item_data)



                    pipeline_distribution_type_0.append(pipeline_distribution_type_0_item)

                return pipeline_distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PipelineStageDistributionDto] | None | Unset, data)

        pipeline_distribution = _parse_pipeline_distribution(d.pop("pipelineDistribution", UNSET))


        opportunity_stats_dto = cls(
            total_open=total_open,
            total_won=total_won,
            total_lost=total_lost,
            total_estimated_value=total_estimated_value,
            total_won_value=total_won_value,
            new_in_period=new_in_period,
            win_rate=win_rate,
            forecast=forecast,
            pipeline_distribution=pipeline_distribution,
        )

        return opportunity_stats_dto

