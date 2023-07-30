import React from "react";
import Typography from "@mui/material/Typography";
import SvgIcon from "@mui/material/SvgIcon";

// Replace the content of the svgPath with your SVG icon's path data
const svgPath = `
  M12.1333 2L12.7827 3.05436C12.9405 3.37736 13.2482 3.59912 13.595 3.59912H18.5539C19.4202 3.59912 19.8575 4.70658 19.2015 5.23895L17.0529 7.21595L19.0905 9.37241C19.6855 10.0818 19.2168 11 18.3941 11H14V15.5C14 16.3284 13.3284 17 12.5 17C11.6716 17 11 16.3284 11 15.5V11H6.60416C5.78146 11 5.31277 10.0818 5.90782 9.37241L7.94546 7.21595L5.79687 5.23895C5.14084 4.70658 5.57818 3.59912 6.44448 3.59912H11.4033C11.7501 3.59912 12.0578 3.37736 12.2156 3.05436L12.865 2H12.1333ZM12.5 5C12.2239 5 12 5.22386 12 5.5V9.5C12 9.77614 12.2239 10 12.5 10C12.7761 10 13 9.77614 13 9.5V5.5C13 5.22386 12.7761 5 12.5 5Z
`;

const logoContainerStyle = {
  display: "flex",
  alignItems: "center",
};

const logoIconStyle = {
  width: 50, // Set the width and height as per your requirement
  height: 50,
  marginRight: 8,
};

const logoTextStyle = {
  fontWeight: "bold",
};

const Logo = () => {
  return (
    <div style={logoContainerStyle}>
      <SvgIcon viewBox="0 0 24 24" style={logoIconStyle}>
        <path d={svgPath} />
      </SvgIcon>
      <Typography variant="h6" style={logoTextStyle}>
        Bug Tracker
      </Typography>
    </div>
  );
};

export default Logo;
