"""TO-DO: Write a description of what this XBlock is."""

import os
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .utils import _


class SummaryXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    display_name = String(
        display_name=_('Display Name'),
        help=_('Display name of the component, which will be shown in the top ribbon.'),
        default='Summary template',
        scope=Scope.content,
        )

    summary = String(
        display_name = _('Summary'),
        default= '',
        scope=Scope.content,
        help= _(''),
        multiline_editor='html',
        )

    editable_fields = (
        'display_name',
        'summary',
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the SummaryXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/summary.html")
        frag = Fragment(html.format(self=self))
        first = self.resource_string("static/js/1.html")
        frag.add_css(self.resource_string("static/css/summary.css"))
        frag.add_javascript(self.resource_string("static/js/src/summary.js"))
        frag.initialize_js('SummaryXBlock')
        frag.add_content(first)
        return frag

    
    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SummaryXBlock",
             """<summary/>
             """),
            ("Multiple SummaryXBlock",
             """<vertical_demo>
                <summary/>
                <summary/>
                <summary/>
                </vertical_demo>
             """),
        ]
