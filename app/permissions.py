from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    
    # função principal...
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        
        if not model_permission_codename:
            return False
        
        return request.user.has_perm(model_permission_codename)
    
    # para montar a string, tipo (genres.view_genre) (app_name.ação_model_name)
    def __get_model_permission_codename(self, method, view):
        try:
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            model_name = view.queryset.model._meta.model_name
            return f'{app_label}.{action}_{model_name}'
            
        except AttributeError:
            return None
    
    # saber qual método está chegando...
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view', 
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            
        }
        return method_actions.get(method, '')