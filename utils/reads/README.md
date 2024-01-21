# Instructions to Generate Bookshelf

## Start Docker (Desktop)

## Run this strictly in powershell in the current directory

```powershell
docker run --rm -v "$(pwd):/data" -u 1000:1000 pandoc/core --standalone --template template/template.html template/reads.md -o reads.html
```

## Move File to Hugo Public Directory

Then place the generated `reads.html` + `reads.js` + `madness.png` in the public directory so it routes to <your-site>/reads
