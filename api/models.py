from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class ProjectTeam(models.Model):
    bussiness_line = models.CharField(max_length=50, null=False)
    team = models.CharField(max_length=50, null=False)
    person = models.CharField(max_length=500, null=False)
    mod_time = models.DateTimeField(u'最后修改日期', auto_now=True)
    create_time = models.DateTimeField(u'保存日期', default=timezone.now)

    def __unicode__(self):
        return self.bussiness_line

    class Meta():
        verbose_name = '基础数据'
        verbose_name_plural = verbose_name
        db_table = 'magic_team_base'


