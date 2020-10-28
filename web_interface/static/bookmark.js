$(document).ready(function(){
    var bookmarked = {{ bookmarked }};
    if (bookmarked){
        $("button").hide();
        $("small").html("{{ game_obj.title }} is bookmarked.");
    }

    $("button").click(function(){
        var confirmed = confirm("Bookmark {{ game_obj.title }}?");
        
        if (confirmed) {
            $.post("/add_bookmark", {
                name: "{{ game_obj.title }}",
                summary: "{{ game_obj.summary }}",
                first_release_date: "{{ game_obj.date_released_timestamp }}",
                rating: {{ game_obj.rating }},
                image_url: "{{ game_obj.image_url }}",
                platforms: "{{ game_obj.platforms }}",
                websites: "{{ game_obj.website_urls }}",
                id: "{{ game_obj.igdb_id }}"
            },
            function(data){ // function run if post is successful
                $("button").hide();
                $("small").html("Bookmarked {{ game_obj.title }}!");
            });
        }
    });
});
