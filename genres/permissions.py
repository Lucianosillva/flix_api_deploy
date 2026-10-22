# from rest_framework import permissions


# class GenrePermissionClass(permissions.BasePermission):
    
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'OPTIONS', 'HEAD']: # safe methods...
#             # nome_app.método a ser executado_nome do model (minúsculo pq está assim no admin)
#             return request.user.has_perm('genres.view_genre')
        
#         if request.method == 'POST':
#             return request.user.has_perm('genres.add_genre')
        
#         if request.method in ['PATCH', 'PUT']:
#             return request.user.has_perm('genres.change_genre')
        
#         if request.method == 'DELETE':
#             return request.user.has_perm('genres.delete_genre')
        
#         return False # padrão