/* Javascript for IntroductionXBlock. */
function IntroductionXBlock(runtime, element) {

    var important_points_holder = document.getElementById("important_points"); /*object for important points section*/
    var definitions_holder = document.getElementById("definitions"); /*object for definition section*/
    var formulae_holder = document.getElementById("formulae"); /*object for formulae section*/
    var handlerUrl = runtime.handlerUrl(element, 'fieldstojs'); /*handler url for fieldtojs function in introduction.py*/

    $(function ($) {
        /* Here's where you'd do things on page load. */
    
        var slideIndex = 0;
        showSlides();

        function showSlides() {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slideIndex++;
            if (slideIndex> slides.length) {slideIndex = 1}
            slides[slideIndex-1].style.display = "block";
            setTimeout(showSlides, 2000); // Change image every 2 seconds
        }
        
        $.ajax({
        type: "POST",
        url: handlerUrl,
        data: JSON.stringify({"hello": "world"}),
        success: updatevariable
        });

        
    });

    /*update variable get through ajax call*/
    function updatevariable(result){
        var jsonparsed = result;
        imp_content = jsonparsed.imp_content;
        def_content = jsonparsed.def_content;
        for_content = jsonparsed.for_content;

        //Hiding important points section if it doesn't have content
        if (imp_content=="") {
            important_points_holder.style.display="none"
        }

        //Hiding definitions section if it doesn't have content
        if (def_content=="") {
            definitions_holder.style.display="none"
        }

        //Hiding formulae section if it doesn't have content
        if (for_content=="") {
            formulae_holder.style.display="none"
        }
    }
}
