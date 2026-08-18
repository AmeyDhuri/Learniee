import { useNavigate } from "react-router-dom"

function Dashboard() {
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem("access_token")
    navigate("/login", { replace: true })
  }

  return (
    <div>
      <h1>Parent Dashboard</h1>
      <p>Dashboard page</p>

      <button onClick={handleLogout}>
        Logout
      </button>
    </div>
  )
}

export default Dashboard