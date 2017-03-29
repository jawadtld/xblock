"""xblock for content template"""

import os
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fields import Integer
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .utils import _


class ContentXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    display_name = String(
        display_name=_('Display Name'),
        help=_('Display name of the component'),
        default="Content template",
        scope=Scope.content)

    subtopic = String(
        display_name=_('Subtopic'),
        default="subtopic",
        scope=Scope.content,
        help=_('Name of subtopic'))

    subtopic_desc = String(
        display_name=_('Subtopic description'),
        default="subtopic description",
        scope=Scope.content,
        help=_('Subtopic description'),
        multiline_editor='html',)

    image_url = String(
        display_name=_('Image URL'),
        default="http://docs.edx.org/edx-docs/assets/images/logo-edx.png",
        scope=Scope.content,
        help=_('Enter url for the image, which will be displayed below the subtopic description'))

    image_desc = String(
        display_name=_('Image description'),
        default="Image description",
        scope=Scope.content,
        help=_('Description for the image'))

    sim_url = String(
        display_name=_('Simulation URL'),
        default="https://phet.colorado.edu/sims/html/states-of-matter/latest/states-of-matter_en.html",
        scope=Scope.content,
        help=_('Enter simulation URL'))

    sim_desc = String(
        display_name=_('Simulation desription'),
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help=_('Small description about the simulation'))

    anim_url = String(
        display_name=_('Animation URL'),
        default="https://www.youtube.com/embed/Fd9a24c1iy4",
        scope=Scope.content,
        help=_('Enter animation URL'))

    anim_desc = String(
        display_name=_('Animation description'),
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help=_('Small description about the animation'))

    vid_url = String(
        display_name=_('Video URL'),
        default="https://www.youtube.com/embed/J_EyP1SAfUo",
        scope=Scope.content,
        help=_('Enter video URL'))

    vid_desc = String(
        display_name=_('Video description'),
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help=_('Small description about the video'))

    game_url = String(
        display_name=_('Game URL'),
        default="http://54.70.206.130/WebGL_Builds/Bowling_WGL/",
        scope=Scope.content,
        help=_('Enter game URL'))

    game_desc = String(
        display_name=_('Game description'),
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help=_('Small description about the game'))

    page_views = Integer(
        display_name=_('Page views'),
        default=0,
        scope=Scope.user_state_summary,
        help=_('Small description about the game'))

    #Editable fields. Editing dialogbox will be rendered based on this entries.
    editable_fields = (
        'display_name',
        'subtopic',
        'subtopic_desc',
        'image_url',
        'image_desc',
        'sim_url',
        'sim_desc',
        'anim_url',
        'anim_desc',
        'vid_url',
        'vid_desc',
        'game_url',
        'game_desc',
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
        self.page_views += 1
        html = self.resource_string("static/html/content.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/content.css"))
        js = self.resource_string("static/js/src/content.js")
        first = self.resource_string("static/js/1.html")
        frag.add_javascript(js)
        frag.initialize_js('ContentXBlock')
        frag.add_content(first)
        return frag

    # It is not possible to access field values using self.<fieldname> inside js file. So we need to
    # pass it through ajax call. We will initiate an ajax call from js file and return needed
    # field values as json.
    @XBlock.json_handler
    def fieldstojs(self, data, suffix=''):
        """
        Used to pass values of fields to content.js
        """
        return {'sim_url':self.sim_url,'anim_url':self.anim_url,'vid_url':self.vid_url,'game_url':self.game_url,'result':'success'}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ContentXBlock",
             """<content/>
             """),
            ("Multiple ContentXBlock",
             """<vertical_demo>
                <content/>
                <content/>
                <content/>
                </vertical_demo>
             """),
        ]
