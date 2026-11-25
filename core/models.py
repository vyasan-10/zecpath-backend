from django.db import models


class User(models.Model):
  ROLE_CHOICES = [
      ('employer', 'Employer'),
      ('candidate', 'Candidate'),
      ('admin', 'Admin'),
  ]
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.name} ({self.role})'


class Employer(models.Model):
  user = models.OneToOneField(
      User, on_delete=models.CASCADE, related_name='employer_profile'
  )
  company_name = models.CharField(max_length=150)
  industry = models.CharField(max_length=100)
  website = models.URLField(blank=True, null=True)
  location = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.company_name


class Candidate(models.Model):
  user = models.OneToOneField(
      User, on_delete=models.CASCADE, related_name='candidate_profile'
  )
  phone = models.CharField(max_length=20)
  skills = models.TextField(help_text='Comma-separated skills for ATS parsing')
  experience_years = models.PositiveIntegerField(default=0)
  resume_url = models.URLField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.name


class Job(models.Model):
  employer = models.ForeignKey(
      Employer, on_delete=models.CASCADE, related_name='jobs'
  )
  title = models.CharField(max_length=150)
  description = models.TextField()
  skills_required = models.TextField()
  location = models.CharField(max_length=100)
  salary_range = models.CharField(max_length=100, blank=True, null=True)
  is_open = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.title} - {self.employer.company_name}'


class Application(models.Model):
  STATUS_CHOICES = [
      ('applied', 'Applied'),
      ('shortlisted', 'Shortlisted'),
      ('interview', 'Interview'),
      ('rejected', 'Rejected'),
      ('hired', 'Hired'),
  ]
  job = models.ForeignKey(
      Job, on_delete=models.CASCADE, related_name='applications'
  )
  candidate = models.ForeignKey(
      Candidate, on_delete=models.CASCADE, related_name='applications'
  )
  status = models.CharField(
      max_length=20, choices=STATUS_CHOICES, default='applied'
  )
  ats_score = models.FloatField(default=0.0)
  applied_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('job', 'candidate')

  def __str__(self):
    return f'{self.candidate.user.name} -> {self.job.title}'