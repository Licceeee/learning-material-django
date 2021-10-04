class CategoryDetailView(DetailView):
    template_name = 'material/topic.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Showcase Section Infos
        context['title'] = _("Category")
        # SEO
        context['page_title'] = _("Category")
        context['page_description'] = _("Category")
        return context
