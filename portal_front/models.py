from django.db import models

# Create your models here.
class PortalFrontSettings(models.Model):
    semaphore_srv_name = models.CharField(max_length=200, verbose_name="Имя")
    semaphore_srv_address = models.CharField(max_length=200, verbose_name="Адрес")
    semaphore_srv_user = models.CharField(max_length=200, verbose_name="Пользователь")
    semaphore_srv_priv_key_file = models.CharField(max_length=200, verbose_name="Приватный ключ")
    semaphore_srv_operator_dir = models.CharField(max_length=200, verbose_name="Папка c файлами")
    copy_files_program = models.CharField(max_length=200, verbose_name="ПО для копирования")

    def __str__(self):
        return self.semaphore_srv_name

    class Meta:
        verbose_name = "Настройка"  
        verbose_name_plural = "Настройки" 
