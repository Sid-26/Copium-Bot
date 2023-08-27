# searchIndex API

The base URL is: [https://search.ezcampus.org/searchIndex/](https://search.ezcampus.org/searchIndex/)

## Schools

### List all schools

GET - /school

#### Example
Request: https://search.ezcampus.org/searchIndex/school
<p>Response: <code>[{"schoolId":1, "schoolUniqueValue":"Ontario Tech University - Canada", "subdomain":"otu", "timezone":"America/Toronto"}, {"schoolId":2, "schoolUniqueValue":"Durham College - Canada", "subdomain":"dc", "timezone":"America/Toronto"}, {"schoolId":3, "schoolUniqueValue":"University of Victoria - Canada", "subdomain":"uv", "timezone":"America/Vancouver"}]</code></p>

### Get school by id

GET - /school/{id}

#### Example
Request: https://search.ezcampus.org/searchIndex/school/1
<p>Response: <code>{"schoolId":1, "schoolUniqueValue":"Ontario Tech University - Canada", "subdomain":"otu", "timezone":"America/Toronto"}</code></p>

### List all terms at a school

POST - /school/term
<p>Fields</p>
<ol>school_name: string</ol>
<ol>school_id: int  (Optional)</ol>

#### Example

Request: https://search.ezcampus.org/searchIndex/school/term \
Body: `{school_name: Ontario Tech - Canada}` \
Response: `[
    {
        "termId": 7,
        "termDescription": "Winter 2022 (View Only)"
    },
    {
        "termId": 6,
        "termDescription": "Spring/Summer 2022 (View Only)"
    }, ...]`

## Classes
### Search for classes for a given term

POST - /search
<p>Fields:</p>
<ul>
<li>search_term: string</li>
<li>page: int</li>
<li>results_per_page: int</li>
<li>term_id: int</li>
<li>search_method: boolean (Optional, defaults to False)</li>
</ul>

The API is based on the Plan Ahead and Register Courses features on the Ontario Tech website.

The search_term field refers to the string that a user enters in order to find courses.

The page and results_per_page fields are self-explanatory, but in this context they serve as selectors for what section of the results should be returned. The courses are returned in order, so a results_per_page of n will return the first n courses. The page number is then used to offset the starting point of the selected courses, using the equation: `offset = results_per_page * (page - 1)`. So a results_per_page of 5 and a page of 2 would return courses 6-10.

The search_method field is just a flag for choosing the method in the backend used when searching.