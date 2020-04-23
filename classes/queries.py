from . import types, models
from graphql_jwt.decorators import login_required


@login_required
def resolve_get_class_list(self, info):
    clasees = models.ClassOrder.objects.all()
    return types.GetClassListReponse(clasees=clasees)


@login_required
def resolve_get_report_cover_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", None)

    if class_order_id != None:
        report_covers = models.ReportCover.objects.filter(
            class_order__pk__in=class_order_id
        )
        return types.GetReportCoverListResponse(reportCovers=report_covers)
    else:
        report_covers = models.ReportCover.objects.all()
        return types.GetReportCoverListResponse(reportCovers=report_covers)


@login_required
def resolve_get_report_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", None)
    class_order_user_uuid = kwargs.get("class_order_user_uuid", None)

    if class_order_id != None:
        reports = models.Report.objects.filter(
            report_cover__class_order__pk__in=class_order_id
        )
        return types.GetReportListResponse(reports=reports)
    elif class_order_user_uuid != None:
        reports = models.Report.objects.filter(
            report_cover__user__uuid=class_order_user_uuid
        )
        return types.GetReportListResponse(reports=reports)
    else:
        reports = models.Report.objects.all()
        return types.GetReportListResponse(reports=reports)
