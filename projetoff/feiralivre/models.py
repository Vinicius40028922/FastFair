from django.db import models


class Topic(models.Model):
    """aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve um representação em string do modelo. """
        return self.text
    
class Entry(models.Model):
    """Algumacoisa"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE )
    text= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve um representação em string do modelo. """
        return self.text[:50] + '...'
