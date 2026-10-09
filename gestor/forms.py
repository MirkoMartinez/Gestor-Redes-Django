from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        # No incluimos 'cliente' porque lo asignaremos automáticamente por detrás
        fields = ['red_social', 'fecha_publicacion', 'texto_posteo', 'estado']
        
        # Le damos el diseño Tailwind y modo oscuro directo desde Python
        estilo_input = 'w-full px-4 py-2 mt-1 border border-slate-300 dark:border-slate-600 rounded-xl bg-white dark:bg-slate-700 focus:ring-2 focus:ring-indigo-500 transition-colors'
        
        widgets = {
            'red_social': forms.TextInput(attrs={'class': estilo_input, 'placeholder': 'Ej: Instagram, LinkedIn'}),
            'fecha_publicacion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': estilo_input}),
            'texto_posteo': forms.Textarea(attrs={'class': estilo_input, 'rows': 3, 'placeholder': 'Escribí el copy acá...'}),
            'estado': forms.Select(attrs={'class': estilo_input}),
        }