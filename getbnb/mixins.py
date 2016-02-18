class MenuItemMixin():
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'menu_item': self.menu_item
        })
        print(ctx)
        return ctx
