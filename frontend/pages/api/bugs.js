import formidable from "formidable";
import fs from "fs";
import path from "path";

const allowedFileTypes = ["image/jpeg", "image/png", "application/pdf"]; // Add more allowed file types as needed

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method === "POST") {
    const form = new formidable.IncomingForm();
    form.parse(req, async (err, fields, files) => {
      if (err) {
        return res.status(500).json({ error: "Error parsing the form data." });
      }

      try {
        const uploadedFiles = [];
        for (const file of Object.values(files)) {
          if (!allowedFileTypes.includes(file.type)) {
            return res.status(400).json({ error: "Invalid file type." });
          }

          const filePath = path.join(
            process.cwd(),
            "public",
            "bugFiles",
            file.name
          );
          await fs.promises.rename(file.path, filePath);

          uploadedFiles.push({
            filename: file.name,
            url: `/bugFiles/${file.name}`,
          });
        }

        return res.status(200).json({ files: uploadedFiles });
      } catch (error) {
        console.error("Error handling file upload:", error);
        return res.status(500).json({ error: "Error handling file upload." });
      }
    });
  } else {
    res.setHeader("Allow", ["POST"]);
    res.status(405).json({ error: `Method ${req.method} not allowed.` });
  }
}
