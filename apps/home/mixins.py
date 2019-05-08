from home.models import University


class SidebarUnies(object):

    def get_unies(self):
        ids = [115, 4, 6, 7, 12, 18, 19, 26, 41, 124]
        universities = (
            University
                .objects
                .filter(id__in=ids)
        )
        return universities
