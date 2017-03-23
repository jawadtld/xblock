/* Javascript for IntroductionXBlock. */
function IntroductionXBlock(runtime, element) {

    var important_points_holder = document.getElementById("important_points");
    var definitions_holder = document.getElementById("definitions");
    var formulae_holder = document.getElementById("formulae");
    var handlerUrl = runtime.handlerUrl(element, 'fieldstojs');

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


    

    function updatevariable(result){
        var jsonparsed = result;
        imp_content = jsonparsed.imp_content;
        def_content = jsonparsed.def_content;
        for_content = jsonparsed.for_content;

        //Hiding additional content tiles which doesn't have values
        if (imp_content=="") {
            important_points_holder.style.display="none"
        }

        if (def_content=="") {
            definitions_holder.style.display="none"
        }

        if (for_content=="") {
            formulae_holder.style.display="none"
        }
    }
}
