from bs4 import BeautifulSoup
html = """
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p class="info">This is a Info Page</p>
    <p class="description">This is a test Page</p>
    <a href="https://sample.com">Visit Sample</a>
</body>
</html>
"""
#Parse the HTML
soup = BeautifulSoup(html,'html.parser')
# Extract title
print("title: ",soup.title.text)
# get Heading
print("Heading: ",soup.h1.text)
#Extract paragraph with class attribute
print("Paragraph",
      soup.find("p",class_="description").text)
#Extract URL
print("links: ",soup.a["href"])