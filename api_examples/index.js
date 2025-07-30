const express = require('express')
const app = express()
const port = 4321

const posts = [
      {
        id: 1,
        description: "¡¡EL MOMENTO MÁS INCREÍBLE EN LA PREMIER LEAGUE!!",
        image: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80",
        user: {
          name: "Invictos",
          image: "https://randomuser.me/api/portraits/men/1.jpg"
        }
      },
      {
        id: 2,
        description: "Messi marca un hat-trick histórico en la Champions League.",
        image: "https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=600&q=80",
        user: {
          name: "Fútbol Total",
          image: "https://randomuser.me/api/portraits/men/2.jpg"
        }
      }
  ]

app.use(express.json())

app.get('/', (req, res) => {
  res.send('Hello World! Probar')
})

app.get('/users', (req, res) => {
  res.send('Christian, Luis')
})

app.get('/posts', (req, res) => {
  res.json({
    posts: posts
  })
})

app.get('/posts/:id', (req, res) => {
  const id = parseInt(req.params.id, 10)
  const post = posts.find(post => post.id === id)
  if (post) {
    res.json(post)
  } else {
    res.status(404).json({ error: 'Post not found' })
  }
})

app.post('/posts', (request, response) => {
  posts.push(request.body)

  response.json({
    posts: posts
  })
})

app.listen(port, () => {
  console.log(`Example app listening on port http://localhost:${port}`)
})

app.use((req, res) => {
  res.status(404).send('Ruta por defecto')
})
// METODOS HTTP
// GET, POST, PUT, PATCH, DELETE

// Endpoint : URL
// https://pokeapi.co/api/v2/pokemon/ditto
