from . import types, models
from classes import models as class_models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_feed_list(self, info):
    user = info.context.user
    try:
        report_cover = class_models.ReportCover.objects.get(
            user=user, report_type="body study"
        )
        feeds = models.Feed.objects.filter(
            class_order__uuid=report_cover.class_order.uuid
        ).order_by("-created_at")
        return types.GetFeedListResponse(feeds=feeds)
    except class_models.ReportCover.DoesNotExist:
        return types.GetFeedListResponse(feeds=None)


@login_required
def resolve_get_feed_list_staff(self, info, **kwargs):
    user = info.context.user
    class_order_uuid = kwargs.get("class_order_uuid")
    try:
        feeds = models.Feed.objects.filter(class_order__uuid=class_order_uuid).order_by(
            "-created_at"
        )
        return types.GetFeedListStaffResponse(feeds=feeds)
    except class_models.ReportCover.DoesNotExist:
        return types.GetFeedListStaffResponse(feeds=None)
