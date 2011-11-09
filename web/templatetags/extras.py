from django.template import Library, Node
from django.conf import settings

from web.models import Comment

register = Library()

class LatestLinksNode(Node):
    def render(self, context):
        context['recent_links'] = Comment.objects.all()[:5]
        return ''

def get_latest_links(parser, token):
    print parser, token
    return LatestLinksNode()

get_latest_links = register.tag(get_latest_links)
