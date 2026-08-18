import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

function Dashboard() {
  const navigate = useNavigate()

  const [user, setUser] = useState(null)
  const [courses, setCourses] = useState([])
  const [pagination, setPagination] = useState({
    page: 1,
    per_page: 6,
    total: 0,
    pages: 0,
    has_next: false,
    has_prev: false,
  })

  const [search, setSearch] = useState("")
  const [subject, setSubject] = useState("")
  const [grade, setGrade] = useState("")
  const [minPrice, setMinPrice] = useState("")
  const [maxPrice, setMaxPrice] = useState("")
  const [minRating, setMinRating] = useState("")
  const [sort, setSort] = useState("default")

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const fetchUser = async () => {
    const token = localStorage.getItem("access_token")

    if (!token) {
      navigate("/login", { replace: true })
      return
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/me", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      const data = await response.json()

      if (!response.ok) {
        localStorage.removeItem("access_token")
        navigate("/login", { replace: true })
        return
      }

      setUser(data)
    } catch (error) {
      console.error("Failed to fetch user:", error)
      setError("Unable to load user information")
    }
  }

  const fetchCourses = async (page = 1) => {
    setLoading(true)
    setError("")

    try {
      const params = new URLSearchParams()

      if (search) params.append("search", search)
      if (subject) params.append("subject", subject)
      if (grade) params.append("grade", grade)
      if (minPrice) params.append("min_price", minPrice)
      if (maxPrice) params.append("max_price", maxPrice)
      if (minRating) params.append("min_rating", minRating)
      if (sort !== "default") params.append("sort", sort)

      params.append("page", page)
      params.append("per_page", 6)

      const response = await fetch(
        `http://127.0.0.1:5000/api/courses?${params.toString()}`
      )

      const data = await response.json()

      if (!response.ok) {
        setError(data.error || "Failed to load courses")
        return
      }

      setCourses(data.courses)
      setPagination(data.pagination)
    } catch (error) {
      setError("Unable to connect to the server")
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchUser()
    fetchCourses()
  }, [])

  const handleSearch = (event) => {
    event.preventDefault()
    fetchCourses(1)
  }

  const handleFilterChange = () => {
    fetchCourses(1)
  }

  const handleLogout = () => {
    localStorage.removeItem("access_token")
    navigate("/login", { replace: true })
  }

  return (
    <div className="dashboard">

      <header className="dashboard-header">
        <div>
          <h1>Course Explorer</h1>
          <p>Find the right course for your child</p>

          {user && (
            <div>
              <p>
                Welcome, <strong>{user.name}</strong> 👋
              </p>
              <p>{user.email}</p>
            </div>
          )}
        </div>

        <button onClick={handleLogout}>
          Logout
        </button>
      </header>

      <main className="dashboard-content">

        <form onSubmit={handleSearch} className="filters">

          <div className="filter-group search-group">
            <label>Search</label>

            <div className="search-row">
              <input
                type="text"
                placeholder="Search courses..."
                value={search}
                onChange={(event) => setSearch(event.target.value)}
              />

              <button type="submit">
                Search
              </button>
            </div>
          </div>

          <div className="filter-grid">

            <div className="filter-group">
              <label>Subject</label>

              <select
                value={subject}
                onChange={(event) => {
                  setSubject(event.target.value)
                  setTimeout(handleFilterChange, 0)
                }}
              >
                <option value="">All Subjects</option>
                <option value="Programming">Programming</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Physics">Physics</option>
                <option value="Chemistry">Chemistry</option>
                <option value="English">English</option>
                <option value="Science">Science</option>
                <option value="Biology">Biology</option>
              </select>
            </div>

            <div className="filter-group">
              <label>Grade</label>

              <select
                value={grade}
                onChange={(event) => {
                  setGrade(event.target.value)
                  setTimeout(handleFilterChange, 0)
                }}
              >
                <option value="">All Grades</option>
                <option value="6">Grade 6</option>
                <option value="7">Grade 7</option>
                <option value="8">Grade 8</option>
                <option value="9">Grade 9</option>
                <option value="10">Grade 10</option>
              </select>
            </div>

            <div className="filter-group">
              <label>Min Price</label>

              <input
                type="number"
                placeholder="₹ Min"
                value={minPrice}
                onChange={(event) => setMinPrice(event.target.value)}
              />
            </div>

            <div className="filter-group">
              <label>Max Price</label>

              <input
                type="number"
                placeholder="₹ Max"
                value={maxPrice}
                onChange={(event) => setMaxPrice(event.target.value)}
              />
            </div>

            <div className="filter-group">
              <label>Minimum Rating</label>

              <select
                value={minRating}
                onChange={(event) => {
                  setMinRating(event.target.value)
                  setTimeout(handleFilterChange, 0)
                }}
              >
                <option value="">Any Rating</option>
                <option value="4">4.0+</option>
                <option value="4.5">4.5+</option>
                <option value="4.7">4.7+</option>
                <option value="4.8">4.8+</option>
                <option value="4.9">4.9+</option>
              </select>
            </div>

            <div className="filter-group">
              <label>Sort By</label>

              <select
                value={sort}
                onChange={(event) => {
                  setSort(event.target.value)
                  setTimeout(handleFilterChange, 0)
                }}
              >
                <option value="default">Default</option>
                <option value="price_asc">Price: Low to High</option>
                <option value="price_desc">Price: High to Low</option>
                <option value="rating_desc">Highest Rating</option>
              </select>
            </div>

          </div>

          <div className="price-filter-button">
            <button type="button" onClick={() => fetchCourses(1)}>
              Apply Price Filters
            </button>
          </div>

        </form>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {loading ? (
          <div className="loading">
            Loading courses...
          </div>
        ) : courses.length === 0 ? (
          <div className="empty-state">
            <h2>No courses found</h2>
            <p>Try changing your search or filters.</p>
          </div>
        ) : (
          <>
            <div className="course-summary">
              <p>
                Showing {courses.length} of {pagination.total} courses
              </p>
            </div>

            <div className="course-grid">

              {courses.map((course) => (
                <div className="course-card" key={course.id}>

                  <div className="course-card-top">
                    <span className="course-subject">
                      {course.subject}
                    </span>

                    <span className="course-rating">
                      ⭐ {course.rating}
                    </span>
                  </div>

                  <h2>{course.name}</h2>

                  <p className="course-teacher">
                    👨‍🏫 {course.teacher}
                  </p>

                  <p className="course-grade">
                    Grade {course.grade}
                  </p>

                  <div className="course-footer">
                    <span className="course-price">
                      ₹{course.price}
                    </span>

                    <button>
                      View Course
                    </button>
                  </div>

                </div>
              ))}

            </div>

            <div className="pagination">

              <button
                disabled={!pagination.has_prev}
                onClick={() => fetchCourses(pagination.page - 1)}
              >
                ← Previous
              </button>

              <span>
                Page {pagination.page} of {pagination.pages}
              </span>

              <button
                disabled={!pagination.has_next}
                onClick={() => fetchCourses(pagination.page + 1)}
              >
                Next →
              </button>

            </div>
          </>
        )}

      </main>
    </div>
  )
}

export default Dashboard