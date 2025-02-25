from typing import Any, Optional, Union

from beartype import beartype
from beartype.typing import Dict

from flet.constrained_control import ConstrainedControl
from flet.control import OptionalNumber
from flet.ref import Ref
from flet.types import (
    AnimationValue,
    MaterialState,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


LabelPosition = Literal[None, "right", "left"]


class Switch(ConstrainedControl):
    def __init__(
        self,
        ref: Optional[Ref] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        #
        # Specific
        #
        label: Optional[str] = None,
        label_position: LabelPosition = None,
        value: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        active_color: Optional[str] = None,
        active_track_color: Optional[str] = None,
        inactive_thumb_color: Optional[str] = None,
        inactive_track_color: Optional[str] = None,
        thumb_color: Union[None, str, Dict[MaterialState, str]] = None,
        track_color: Union[None, str, Dict[MaterialState, str]] = None,
        on_change=None,
        on_focus=None,
        on_blur=None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )
        self.value = value
        self.label = label
        self.label_position = label_position
        self.autofocus = autofocus
        self.active_color = active_color
        self.active_track_color = active_track_color
        self.inactive_thumb_color = inactive_thumb_color
        self.inactive_track_color = inactive_track_color
        self.thumb_color = thumb_color
        self.track_color = track_color
        self.on_change = on_change
        self.on_focus = on_focus
        self.on_blur = on_blur

    def _get_control_name(self):
        return "switch"

    def _before_build_command(self):
        super()._before_build_command()
        self._set_attr_json("thumbColor", self._wrap_attr_dict(self.__thumb_color))
        self._set_attr_json("trackColor", self._wrap_attr_dict(self.__track_color))

    # value
    @property
    def value(self) -> Optional[bool]:
        return self._get_attr("value", data_type="bool", def_value=False)

    @value.setter
    @beartype
    def value(self, value: Optional[bool]):
        self._set_attr("value", value)

    # label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

    # label_position
    @property
    def label_position(self) -> LabelPosition:
        return self._get_attr("labelPosition")

    @label_position.setter
    @beartype
    def label_position(self, value: LabelPosition):
        self._set_attr("labelPosition", value)

    # autofocus
    @property
    def autofocus(self) -> Optional[bool]:
        return self._get_attr("autofocus", data_type="bool", def_value=False)

    @autofocus.setter
    @beartype
    def autofocus(self, value: Optional[bool]):
        self._set_attr("autofocus", value)

    # active_color
    @property
    def active_color(self):
        return self._get_attr("activeColor")

    @active_color.setter
    def active_color(self, value):
        self._set_attr("activeColor", value)

    # active_track_color
    @property
    def active_track_color(self):
        return self._get_attr("activeTrackColor")

    @active_track_color.setter
    def active_track_color(self, value):
        self._set_attr("activeTrackColor", value)

    # inactive_thumb_color
    @property
    def inactive_thumb_color(self):
        return self._get_attr("inactiveThumbColor")

    @inactive_thumb_color.setter
    def inactive_thumb_color(self, value):
        self._set_attr("inactiveThumbColor", value)

    # inactive_track_color
    @property
    def inactive_track_color(self):
        return self._get_attr("inactiveTrackColor")

    @inactive_track_color.setter
    def inactive_track_color(self, value):
        self._set_attr("inactiveTrackColor", value)

    # thumb_color
    @property
    def thumb_color(self) -> Union[None, str, Dict[MaterialState, str]]:
        return self.__thumb_color

    @thumb_color.setter
    @beartype
    def thumb_color(self, value: Union[None, str, Dict[MaterialState, str]]):
        self.__thumb_color = value

    # track_color
    @property
    def track_color(self) -> Union[None, str, Dict[MaterialState, str]]:
        return self.__track_color

    @track_color.setter
    @beartype
    def track_color(self, value: Union[None, str, Dict[MaterialState, str]]):
        self.__track_color = value

    # on_change
    @property
    def on_change(self):
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler):
        self._add_event_handler("change", handler)

    # on_focus
    @property
    def on_focus(self):
        return self._get_event_handler("focus")

    @on_focus.setter
    def on_focus(self, handler):
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    def on_blur(self):
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler):
        self._add_event_handler("blur", handler)
