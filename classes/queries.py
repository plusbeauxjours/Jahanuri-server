from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_class_list(self, info):
    clasees = models.ClassOrder.objects.all()
    return types.GetClassListReponse(clasees=clasees)


@login_required
def resolve_get_report_cover_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", "")

    if class_order_id != "":
        report_covers = models.ReportCover.objects.filter(
            class_order__pk__in=class_order_id
        )
        return types.GetReportCoverListResponse(reportCovers=report_covers)
    else:
        return types.GetReportCoverListResponse(reportCovers=None)


@login_required
def resolve_get_report_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", "")
    user_uuid = kwargs.get("user_uuid", "")

    if class_order_id != "":
        reports = models.Report.objects.filter(
            report_cover__class_order__pk__in=class_order_id
        )
        return types.GetReportListResponse(reports=reports)
    elif user_uuid != "":
        reports = models.Report.objects.filter(report_cover__user__uuid=user_uuid)
        return types.GetReportListResponse(reports=reports)
    else:
        return types.GetReportListResponse(reports=None)
