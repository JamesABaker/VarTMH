from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Database_Metadata(models.Model):
    last_run = models.DateTimeField(default=timezone.now)
    last_download = models.DateTimeField(default=timezone.now)

class Protein(models.Model):
    uniprot_id = models.CharField(max_length=20, unique=True)
    full_sequence = models.TextField()
    #total_tmh_number = models.IntegerField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)


class Tmh(models.Model):
    # Several features should map to  a protein.
    protein = models.ForeignKey(Protein, on_delete=models.CASCADE)

    # These may be useful on the webserver.
    tmh_id = models.TextField(unique=True)

    # tmh include the TMHs and stretches of protein.
    tmh_sequence = models.TextField()
    tmh_start = models.IntegerField()
    tmh_stop = models.IntegerField()
    tmh_evidence = models.TextField()
    tmh_number = models.IntegerField()
    tmh_total_number = models.IntegerField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    membrane_type = models.CharField(max_length=100, default='')
    n_terminal_inside = models.CharField(max_length=100, default='')


class Tmh_tmsoc(models.Model):

    # Originally I thought this would be good for scores and results from
    # sequence analysis.
    tmh = models.ForeignKey(Tmh, on_delete=models.CASCADE)

    # In order to keep things generic I think it is best to fragment test results.
    # So for example, if TMSOC gives an output of "Complex" and "2.7" this would
    # give 2 separate entries both tied to the tmh.
    test_type = models.TextField()
    test_result = models.TextField()
    test_score = models.FloatField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    # This also needs to have a tmh number. For example, we need to ask the question is this tmh 1 of 1 or 1 of 7. Can this information be obtained from elsewhere?


class Tmh_deltag(models.Model):

    # Originally I thought this would be good for scores and results from
    # sequence analysis.
    tmh = models.ForeignKey(Tmh, on_delete=models.CASCADE)

    # In order to keep things generic I think it is best to fragment test results.
    # So for example, if TMSOC gives an output of "Complex" and "2.7" this would
    # give 2 separate entries both tied to the tmh.
    test_type = models.TextField()
    #test_result = models.TextField()
    test_score = models.FloatField(default=None)
    created_date = models.DateTimeField(default=timezone.now)
    # This also needs to have a tmh number. For example, we need to ask the question is this tmh 1 of 1 or 1 of 7. Can this information be obtained from elsewhere?


class Tmh_hydrophobicity(models.Model):
    tmh = models.ForeignKey(Tmh, on_delete=models.CASCADE)

    aromaticity = models.FloatField(default=None)
    flexibility = models.TextField()

    kyte_avg = models.FloatField(default=None)
    ww_avg = models.FloatField(default=None)
    eisenberg_avg = models.FloatField(default=None)

    kyte_window = models.TextField()
    ww_window = models.TextField()
    eisenberg_window = models.TextField()


class Residue(models.Model):
    protein = models.ForeignKey(Protein, on_delete=models.CASCADE)
    amino_acid_type = models.CharField(max_length=1, default='')
    sequence_position = models.IntegerField()

    class Meta:
        unique_together = ["protein", "sequence_position"]


class Tmh_residue(models.Model):
    protein = models.ForeignKey(Residue, on_delete=models.CASCADE)
    amino_acid_type = models.CharField(max_length=1, default='')
    amino_acid_location = models.IntegerField(default=None)


class Variant(models.Model):
    aa_wt = models.CharField(max_length=1, default='')
    aa_mut = models.CharField(max_length=1, default='')
    residue = models.ForeignKey(Residue, on_delete=models.CASCADE)
    disease_status = models.TextField()  # either disease or benign or uncertain
    disease_comments = models.TextField()
    variant_source = models.TextField(default="Unknown")
