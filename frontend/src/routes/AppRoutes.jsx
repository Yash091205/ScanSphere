import { BrowserRouter, Routes, Route } from "react-router-dom";

import HomePage from "../pages/HomePage";
import UploadPage from "../pages/UploadPage";
import ReviewPage from "../pages/ReviewPage";
import EnhancementReviewPage from "../pages/EnhancementReviewPage";
import OCRReviewPage from "../pages/OCRReviewPage";
import DownloadPage from "../pages/DownloadPage";

export default function AppRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/upload" element={<UploadPage />} />
                <Route path="/review" element={<ReviewPage />} />
                <Route path="/enhancement-review" element={<EnhancementReviewPage />}/>
                <Route path="/ocr" element={<OCRReviewPage />} />
                <Route path="/download" element={<DownloadPage />} />
            </Routes>
        </BrowserRouter>
    );
}