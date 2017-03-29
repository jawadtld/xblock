"""Xblock for introduction"""

import os
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .utils import _


class IntroductionXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    display_name = String(
        display_name=_('Display Name'),
        help=_('Display name of the component, which will be shown in the top ribbon.'),
        default='Introduction template',
        scope=Scope.content,
        )

    title = String(
        display_name = _('Title'),
        default= 'Unit title',
        scope=Scope.content,
        help= _('Enter unit name.'),
        )

    title_bg = String(
        display_name= _('Background image for title'),
        default= '/static/force_banner.jpg',
        scope=Scope.content,
        help= _('Title background image url. Recommended size of image is 800x200 pixels.'),
        )

    intro_content = String(
        display_name =_('Introduction'),
        default='',
        scope=Scope.content,
        help=_(''),
        multiline_editor='html',
        )

    slide1 = String(
        display_name=_('Slide show image1') ,
        default='/static/slider1.jpg',
        scope=Scope.content,
        help=_('Image url for first image in slideshow'),
        )

    slide2 = String(
        display_name=_('Slide show image2') ,
        default='/static/slider2.jpg',
        scope=Scope.content,
        help=_('Image url for second image in slideshow. Image size should be same as of above image.'),
        )

    imp_content = String(
        display_name = _('Important points'),
        default='',
        scope=Scope.content,
        help=_(''),
        multiline_editor='html',
        )

    def_content = String(
        display_name = _('Definitions'),
        default='',
        scope=Scope.content,
        help=_(''),
        multiline_editor='html',
        )

    for_content = String(
        display_name = _('Formulae'),
        default='',
        scope=Scope.content,
        help=_(''),
        multiline_editor='html',
        )

    #Editable fields. Editing dialogbox will be rendered based on this entries.
    editable_fields = (
        'display_name',
        'title',
        'title_bg',
        'intro_content',
        'slide1',
        'slide2',
        'imp_content',
        'def_content',
        'for_content',
    )


    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ContentXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/introduction.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/introduction.css"))
        js = self.resource_string("static/js/src/introduction.js")
        first = self.resource_string("static/js/1.html")
        frag.add_javascript(js)
        frag.initialize_js('IntroductionXBlock')
        frag.add_content(first)
        return frag

    # It is not possible to access field values using self.<fieldname> inside js file. So we need to
    # pass it through ajax call. We will initiate an ajax call from js file and return needed
    # field values as json.
    @XBlock.json_handler
    def fieldstojs(self, data, suffix=''):
        """
        Used to pass values of fields to introduction.js
        """
        return {'imp_content':self.imp_content,'def_content':self.def_content,'for_content':self.for_content,'result':'success'}




    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("IntroductionXBlock",
             """<introduction/>
             """),
            ("Multiple IntroductionXBlock",
             """<vertical_demo>
                <introduction/>
                <introduction/>
                <introduction/>
                </vertical_demo>
             """),
        ]
