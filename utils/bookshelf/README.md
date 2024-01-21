# Instructions to Generate Bookshelf

## Start Docker (Desktop)

## Run this strictly in powershell in the current directory

```powershell
docker run --rm -v "$(pwd):/data" -u 1000:1000 pandoc/core --standalone --template template/template.html template/books.md -o index.html
```

## Move File to Hugo Public Directory

Then place the generated `index.html` in the public directory and make sure you rename it to `bookshelf.html` so it routes to <your-site>/bookshelf
