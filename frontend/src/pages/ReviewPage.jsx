import MainLayout from "../layouts/MainLayout";

import ReviewGallery from "../components/review/ReviewGallery";

import useReviewActions from "../hooks/useReviewActions";

export default function ReviewPage() {

    const {

        loading,

        session,

    } = useReviewActions();

    if (loading) {

        return (
            <MainLayout>

                <h2>Loading...</h2>

            </MainLayout>
        );

    }

    return (

        <MainLayout>

            <h1 className="text-4xl font-bold mb-8">

                Review Uploaded Pages

            </h1>

            <ReviewGallery
                pages={session.pages}
            />

        </MainLayout>

    );

}