import { useNavigate } from "react-router-dom";
import MDButton from "components/MDButton";

function LogoutButton() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");

    navigate("/authentication/sign-in");
  };

  return (
    <MDButton variant="gradient" color="error" fullWidth onClick={logout}>
      LOGOUT
    </MDButton>
  );
}

export default LogoutButton;
